from django.shortcuts import render, redirect



def auth_middleware(get_response):
    def middleware(request):
        print('Middle ware')
        response = get_response(request)
        uid = request.session.get('customer')
        if not uid:
            return redirect('login')
        return response
    return middleware