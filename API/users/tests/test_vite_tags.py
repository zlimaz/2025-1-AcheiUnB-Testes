import json
import os
from unittest.mock import mock_open, patch

from django.conf import settings
from django.test import TestCase

from users.templatetags.vite_tags import vite_asset


class ViteAssetTagTests(TestCase):
    def setUp(self):
        self.manifest_mock = {
            "index.html": {
                "file": "assets/index.abc123.js",
                "css": ["assets/style.abc123.css"],
            },
            "about.html": {
                "file": "assets/about.def456.js",
            },
        }

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            {
                "index.html": {
                    "file": "assets/index.abc123.js",
                    "css": ["assets/style.abc123.css"],
                },
                "about.html": {
                    "file": "assets/about.def456.js",
                },
            }
        ),
    )
    @patch(
        "users.templatetags.vite_tags.MANIFEST_PATH",
        os.path.join(settings.BASE_DIR, "manifest.json"),
    )
    def test_vite_asset_js(self, mock_manifest):
        """Testa se retorna o caminho correto do arquivo JS."""
        result = vite_asset("index.html", "js")
        assert result.startswith("/static/dist/")
        assert result.endswith(".js")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            {
                "index.html": {
                    "file": "assets/index.abc123.js",
                    "css": ["assets/style.abc123.css"],
                },
                "about.html": {
                    "file": "assets/about.def456.js",
                },
            }
        ),
    )
    @patch(
        "users.templatetags.vite_tags.MANIFEST_PATH",
        os.path.join(settings.BASE_DIR, "manifest.json"),
    )
    def test_vite_asset_css(self, mock_manifest):
        """Testa se retorna o caminho correto do arquivo CSS."""
        result = vite_asset("index.html", "css")
        assert result.startswith("/static/dist/")
        assert result.endswith(".css")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            {
                "index.html": {
                    "file": "assets/index.abc123.js",
                    "css": ["assets/style.abc123.css"],
                },
                "about.html": {
                    "file": "assets/about.def456.js",
                },
            }
        ),
    )
    @patch(
        "users.templatetags.vite_tags.MANIFEST_PATH",
        os.path.join(settings.BASE_DIR, "manifest.json"),
    )
    def test_vite_asset_missing_entry(self, mock_manifest):
        """Testa se retorna string vazia quando a entrada não está no manifest."""
        result = vite_asset("nonexistent.html", "js")
        assert result == ""

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            {
                "index.html": {
                    "file": "assets/index.abc123.js",
                    "css": ["assets/style.abc123.css"],
                },
                "about.html": {
                    "file": "assets/about.def456.js",
                },
            }
        ),
    )
    @patch(
        "users.templatetags.vite_tags.MANIFEST_PATH",
        os.path.join(settings.BASE_DIR, "manifest.json"),
    )
    def test_vite_asset_missing_css(self, mock_manifest):
        """Testa se retorna string vazia quando não há CSS na entrada."""
        result = vite_asset("about.html", "css")
        assert result == ""

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            {
                "index.html": {
                    "file": "assets/index.abc123.js",
                    "css": ["assets/style.abc123.css"],
                },
                "about.html": {
                    "file": "assets/about.def456.js",
                },
            }
        ),
    )
    @patch(
        "users.templatetags.vite_tags.MANIFEST_PATH",
        os.path.join(settings.BASE_DIR, "manifest.json"),
    )
    def test_vite_asset_invalid_type(self, mock_manifest):
        """Testa se retorna string vazia para um tipo de asset inválido."""
        result = vite_asset("index.html", "invalid")
        assert result == ""
