import Portfolio from '../pages/Portfolio.vue'
import SnotelProject from '../pages/projects/snotel/SnotelProject'

import RideShareServicesProject from '../pages/projects/microservices/rideshare-services/RideShareServicesProject'
import HealthCareServicesProject from '../pages/projects/microservices/healthcare-services/HealthCareServicesProject'
import EComServicesProject from '../pages/projects/microservices/ecomm-services/EComServicesProject'


import SamECommProject from '../pages/projects/serverless/sam-ecommerce/SamECommProject'
import ServerlessDataProject from '../pages/projects/serverless/data-applications/ServerlessDataProject'
import ServerlessUploadProject from '../pages/projects/serverless/serverless-upload/ServerlessUploadProject'


import TwitterPipelineProject from '../pages/projects/twitter/pipeline/TwitterPipelineProject'
import TwitterQueryApiProject from '../pages/projects/twitter/query-api/TwitterQueryApiProject'

import MirProject from '../pages/projects/deep-learning/mir/MirProject'
import NmtProject from '../pages/projects/deep-learning/nmt/NmtProject'

import TwitterNlpProject from '../pages/projects/analytics/TwitterNLP/TwitterNlpProject'

import ProjectDetail from '../pages/ProjectDetail'

import PostPortfolioArticle from '../pages/post/PostPortfolioArticle'

export default [
	{ path: '', component: Portfolio },
	{ path: '/portfolio', component: Portfolio },

	// { path: '/portfolio/detail/:article_category/:article_name', component: ProjectDetail, name:'portfolio_detail', props:true },
	{ path: '/portfolio/detail', component: ProjectDetail},


	{ path: '/portfolio/snotel', component: SnotelProject },

	{ path: '/portfolio/microservices/rideshare', component: RideShareServicesProject },
	{ path: '/portfolio/microservices/healthcare', component: HealthCareServicesProject},
	{ path: '/portfolio/microservices/ecomm', component: EComServicesProject},


	{ path: '/portfolio/serverless/ecommerce', component: SamECommProject },
	{ path: '/portfolio/serverless/data-processing', component: ServerlessDataProject},
	{ path: '/portfolio/serverless/upload', component: ServerlessUploadProject},

	{ path: '/portfolio/twitter/pipeline', component: TwitterPipelineProject},
	{path: '/portfolio/twitter/query-api', component: TwitterQueryApiProject},

	{path: '/portfolio/deep-learning/mir', component: MirProject},
	{path: '/portfolio/deep-learning/nmt', component: NmtProject},

	{path: '/portfolio/analytics/twitternlp', component: TwitterNlpProject},


	{path: '/portfolio/post', component: PostPortfolioArticle, name:'post_portfolio_article'}

]
