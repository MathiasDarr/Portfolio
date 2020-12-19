
import Blog from '../pages/Blog'
import Article from '../pages/articles/Article'


export default [
	{ path: '', component: Blog },
	{ path: '/blog', component: Blog },
	{ path: '/blog/article/:article_id', component: Article, name:'article' }

]
