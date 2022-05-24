from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        nickname = data.get("nickname")
        profile_image = data.get("profile_image")
        using_ott = data.get("using_ott")
        if nickname:
            user.nickname = nickname
        if profile_image:
            user.profile_image = profile_image
        if using_ott:
            user.using_ott = using_ott

        user.save()
        return user