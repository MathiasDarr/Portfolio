/* eslint-disable */



import Blog from '../pages/Blog'
// import Article from '../pages/articles/Article'
import PostArticle from '../pages/post/PostArticle'
import ArticleDetail from '../pages/articles/ArticleDetail'
import Index from '../pages/Index'
export default [
	{ path: '', component: Index },
	{ path: '/index', component: Index },
	{ path: '/blog', component: Blog , name:'blog'},
	{ path: '/blog/article/:article_id', component: ArticleDetail, name:'article', props:true },
	{path: '/blog/article/post', component: PostArticle, name:'post_article'},
]
