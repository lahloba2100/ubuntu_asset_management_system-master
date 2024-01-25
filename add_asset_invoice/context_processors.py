def user_info(request):
    user_info = {}
    if request.user.is_authenticated:
        user_info['username'] = request.user.username
    return {'user_info': user_info}
