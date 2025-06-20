# api/users/tests/test_item_serializer.py

from unittest.mock import patch, MagicMock
from django.test import TestCase
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import pytest # Importar pytest para pytest.approx

# Importe o ItemSerializer da localização correta no seu projeto
from API.users.serializers import ItemSerializer 

# Importa as tarefas diretamente para que possamos referenciá-las nos patches
from API.users.tasks import remove_images_from_item, upload_images_to_cloudinary

# Patchamos as funções 'delay' diretamente nos módulos onde elas são definidas
# Ou, se o patch deve ser onde elas são USADAS, o caminho dentro do serializer seria:
# 'api.users.serializers.remove_images_from_item.delay'
# 'api.users.serializers.upload_images_to_cloudinary.delay'

# Vamos usar o patch no local onde elas são REFERENCIADAS no serializer para garantir que funcione.
@patch('api.users.serializers.remove_images_from_item.delay') # <-- PATCH CORRIGIDO
@patch('api.users.serializers.upload_images_to_cloudinary.delay') # <-- PATCH CORRIGIDO
class ItemSerializerUpdateTests(TestCase): # Usamos TestCase pois é um teste de Django/DRF

    def setUp(self):
        # Instancia o serializer para cada teste
        self.serializer = ItemSerializer()
        
        # Cria um mock para a 'instance' (o objeto Item que está sendo atualizado)
        # É importante que ele se pareça com um Item de verdade para o serializer.
        self.mock_item_instance = MagicMock() 
        self.mock_item_instance.id = 1 # ID do item para mockar
        
        # Mocka o manager 'images' da instância para controlar .count()
        self.mock_item_instance.images.count.return_value = 0 

        # Mocks para as novas imagens que seriam enviadas
        self.mock_image_file_1 = MagicMock(spec=object)
        self.mock_image_file_1.file.read.return_value = b'image_data_1' # Simula leitura do arquivo
        self.mock_image_file_2 = MagicMock(spec=object)
        self.mock_image_file_2.file.read.return_value = b'image_data_2'
        self.mock_image_file_3 = MagicMock(spec=object)
        self.mock_image_file_3.file.read.return_value = b'image_data_3'

        # Mocks para o método super().update do ModelSerializer
        # Patchamos o método 'update' DA CLASSE PAI (serializers.ModelSerializer)
        # como ele é chamado pelo super()
        self.patcher_super_update = patch('rest_framework.serializers.ModelSerializer.update')
        self.mock_super_update = self.patcher_super_update.start()
        self.mock_super_update.return_value = self.mock_item_instance # super().update retorna a instance atualizada

    def tearDown(self):
        # Limpa os mocks após cada teste
        self.patcher_super_update.stop()


    # --- Testes Base (não MC/DC, mas importantes para cobertura de decisão) ---

    def test_ct1_update_sem_imagens_sem_remocao(self, mock_upload_cloudinary, mock_remove_images):
        # CT1: Atualizar item - Sem imagens (base)
        # CD1F, CD2F(0,0), CD3F(0,0), CD4F - D2: ID 1
        
        validated_data = {"name": "Novo Nome"}
        
        updated_item = self.serializer.update(self.mock_item_instance, validated_data)

        self.assertEqual(updated_item, self.mock_item_instance) # Verifica se retornou a instância mockada
        self.mock_super_update.assert_called_once_with(self.mock_item_instance, validated_data)
        mock_remove_images.delay.assert_not_called()
        mock_upload_cloudinary.delay.assert_not_called()

    def test_ct2_update_removendo_imagens(self, mock_upload_cloudinary, mock_remove_images):
        # CT2: Atualizar item - Remover imagens
        # CD1V, CD2F(X,0), CD3F(X,0), CD4F
        
        validated_data = {"remove_images": [101, 102]} # IDs de imagens para remover
        
        updated_item = self.serializer.update(self.mock_item_instance, validated_data)

        self.assertEqual(updated_item, self.mock_item_instance)
        self.mock_super_update.assert_called_once_with(self.mock_item_instance, validated_data)
        mock_remove_images.delay.assert_called_once_with([101, 102]) # Verifica se a tarefa de remoção foi chamada
        mock_upload_cloudinary.delay.assert_not_called()

    # --- Testes MC/DC para Decisão D2 (if instance.images.count() + len(images) > MAX_IMAGES:) ---

    def test_ct3_mcdc_excede_limite_cd2_v(self, mock_upload_cloudinary, mock_remove_images):
        # CT3: Atualizar item - Exceder limite - Par 1 MC/DC (CD2-V)
        # C_EXIST=1, C_NOVAS=2 => (1+2=3) > 2 (True) - D2: ID 7
        
        self.mock_item_instance.images.count.return_value = 1 # 1 imagem existente
        validated_data = {"images": [self.mock_image_file_1, self.mock_image_file_2]} # 2 novas imagens

        with pytest.raises(ValidationError) as excinfo:
            self.serializer.update(self.mock_item_instance, validated_data)
        
        self.assertIn("Você pode adicionar no máximo 2 imagens.", str(excinfo.value))
        self.mock_super_update.assert_not_called() # Não deve chamar super().update em caso de erro
        mock_remove_images.delay.assert_not_called()
        mock_upload_cloudinary.delay.assert_not_called()

    def test_ct4_mcdc_nao_excede_limite_cd2_f(self, mock_upload_cloudinary, mock_remove_images):
        # CT4: Atualizar item - Não exceder limite - Par 1 MC/DC (CD2-F)
        # C_EXIST=0, C_NOVAS=2 => (0+2=2) > 2 (False) - D2: ID 3
        
        self.mock_item_instance.images.count.return_value = 0 # 0 imagens existentes
        validated_data = {"images": [self.mock_image_file_1, self.mock_image_file_2]} # 2 novas imagens

        updated_item = self.serializer.update(self.mock_item_instance, validated_data)

        self.assertEqual(updated_item, self.mock_item_instance)
        self.mock_super_update.assert_called_once_with(self.mock_item_instance, validated_data)
        mock_upload_cloudinary.delay.assert_called_once_with(
            self.mock_item_instance.id, [b'image_data_1', b'image_data_2']
        )
        mock_remove_images.delay.assert_not_called()

    def test_ct5_mcdc_excede_limite_cd3_v(self, mock_upload_cloudinary, mock_remove_images):
        # CT5: Atualizar item - Exceder limite - Par 2 MC/DC (CD3-V)
        # C_EXIST=2, C_NOVAS=1 => (2+1=3) > 2 (True) - D2: ID 9
        
        self.mock_item_instance.images.count.return_value = 2 # 2 imagens existentes
        validated_data = {"images": [self.mock_image_file_1]} # 1 nova imagem

        with pytest.raises(ValidationError) as excinfo:
            self.serializer.update(self.mock_item_instance, validated_data)
        
        self.assertIn("Você pode adicionar no máximo 2 imagens.", str(excinfo.value))
        self.mock_super_update.assert_not_called()
        mock_remove_images.delay.assert_not_called()
        mock_upload_cloudinary.delay.assert_not_called()

    def test_ct6_mcdc_nao_excede_limite_cd3_f(self, mock_upload_cloudinary, mock_remove_images):
        # CT6: Atualizar item - Não exceder limite - Par 2 MC/DC (CD3-F)
        # C_EXIST=2, C_NOVAS=0 => (2+0=2) > 2 (False) - D2: ID 8
        
        self.mock_item_instance.images.count.return_value = 2 # 2 imagens existentes
        validated_data = {"name": "Outro Nome"} # Nenhuma nova imagem, len(images) = 0

        updated_item = self.serializer.update(self.mock_item_instance, validated_data)

        self.assertEqual(updated_item, self.mock_item_instance)
        self.mock_super_update.assert_called_once_with(self.mock_item_instance, validated_data)
        mock_upload_cloudinary.delay.assert_not_called() # Não deve chamar upload se não há imagens novas
        mock_remove_images.delay.assert_not_called()