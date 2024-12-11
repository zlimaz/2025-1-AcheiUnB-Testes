from django.dispatch import receiver


def update_user_profile(request, user, **kwargs):
    social_account = SocialAccount.objects.filter(
        user=user, provider="microsoft"
    ).first()

    if social_account:
        extra_data = social_account.extra_data
        user.first_name = extra_data.get("givenName", user.first_name)
        user.last_name = extra_data.get("surname", user.last_name)
        user.email = extra_data.get("mail", user.email)

        # Extração da matrícula
        if user.email and "@aluno.unb.br" in user.email:
            user.username = user.email.split("@")[0]

        user.save()
