const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',

    currentUserInfo: () => HOST + ACCOUNTS + 'user/',

    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },

  movies: {
    movies: () => HOST + MOVIES,
    movie: movieId => HOST + MOVIES + `${movieId}/`,
    boxoffices: () => HOST + MOVIES + 'boxoffice/',
    boxoffices_ind: () => HOST + MOVIES + 'boxoffice/independent/',
    likemovie: movieId => HOST + MOVIES + `${movieId}/` + 'like/',
    watchedmovie: movieId => HOST + MOVIES + `${movieId}/` + 'watch/',
    reviews: movieId => HOST + MOVIES + `${movieId}/` + 'review/',
    review: (movieId, reviewPk) => HOST + MOVIES + `${movieId}/` + 'review/' `${reviewPk}/` ,
    likeReview: (movieId, reviewPk) => HOST + MOVIES + `${movieId}/` + 'review/' `${reviewPk}/` + 'like/' ,
    recommendationLike: () => HOST + MOVIES + 'recommendation/' + 'like/',
    recommendationWatch: () => HOST + MOVIES + 'recommendation/' + 'watch/',
    recommendationNetflix: () => HOST + MOVIES + 'recommendation/' + 'netflix/',
    recommendationWatcha: () => HOST + MOVIES + 'recommendation/' + 'watcha/',
    recommendationWavve: () => HOST + MOVIES + 'recommendation/' + 'wavve/',
    recommendationDisney: () => HOST + MOVIES + 'recommendation/' + 'disney/',
  },

  articles: {
    articles: () => HOST + ARTICLES,
    events: () => HOST + ARTICLES + 'event/',
    news: () => HOST + ARTICLES + 'news/',
    column: () => HOST + ARTICLES + 'column/',
    board: () => HOST + ARTICLES + 'board/',
    sinye: () => HOST + ARTICLES + 'sinye/',

    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  }
}
