def check_article_view():
    try:
        return request.session["read_articles"]
    except:
        request.session["read_articles"] = []
        return request.session["read_articles"] 
    else:
        return request.sesssion["read_articles"]
        
def chek_article_view(request, article_id):
    read_articles = check_read_articles(request)
    if aricle_id in read_articles:
        print("article read...")
        return False
    else:
        request.session["read_articles"].append(article_id)
        print("article views updtaed")
        return True
    
    