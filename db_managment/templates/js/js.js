// function SetArticleRating(rating, article_id) {
//     console.log(rating)
//     console.log(article_id)
// }

function SetArticleRating(rating, article_id) {
    let params = {
        method: "post",
        body: JSON.stringify(
            {
                rating: rating,
                article_id: article_id
            }
        )
    }
    fetch('/add/rating/', params)
    .then(response => response.json())
    .then(data =>console.log(data))
}