function getCookie(name) {
    if (!document.cookie) {
      return null;
    }
  
    const xsrfCookies = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith(name + '='));
  
    if (xsrfCookies.length === 0) {
      return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
  }

  const csrfToken = getCookie('CSRF-TOKEN');

function SetArticleRating(rating,article_id){
    let article = document.querySelector("#article_rating")
    let data = JSON.stringify(
        {
            rating:rating,
            article_id:article_id
        }
    )

    let url = `/posts/add/rating/?data=${data}`

    fetch(url) 
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

}