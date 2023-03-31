def check_article_view():
    try:
        return request.session["read_articles"]
    except:
        request.session["read_articles"] = []
        return request.session["read_articles"] 
    else:
        return request.sesssion["read_articles"]
        
def chek_article_view(request, article_id):
    request.session.modified = True
    a_list = check_read_articles(request)
    if aricle_id in a_list:
        print("article read...")
        return False
    else:
        a_list.append(article_id)
        print("article views updtaed")
        return True
    
    