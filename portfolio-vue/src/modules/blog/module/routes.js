
import Blog from '../pages/Blog'
import Article from '../pages/articles/Article'
import PostArticle from '../pages/PostArticle'


export default [
	{ path: '', component: Blog },
	{ path: '/blog', component: Blog },
	{ path: '/blog/article/:article_id', component: Article, name:'article' },
	{path: '/blog/article/post', component: PostArticle, name:'post_article'}

]
