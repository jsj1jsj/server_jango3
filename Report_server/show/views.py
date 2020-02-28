from django.shortcuts import render
# from django.shortcuts import render,render_to_response,get_object_or_404

def showReport(request):
    # return render_to_response("report.html")
    return render(request,"report.html",{"name":"test","password":"123456"})



# return render(request,"information.html",{"name":"test","password":"123456"})

# return render_to_response("information.html",{"name":"test","password":"123456"},context_instance = RequestContext(request))


