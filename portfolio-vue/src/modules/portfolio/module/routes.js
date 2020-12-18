import Portfolio from '../pages/Portfolio.vue'
import SnotelProject from '../pages/projects/snotel/SnotelProject'

import RideShareServicesProject from '../pages/projects/microservices/rideshare-services/RideShareServicesProject'
import HealthCareServicesProject from '../pages/projects/microservices/healthcare-services/HealthCareServicesProject'

import SamECommProject from '../pages/projects/serverless/sam-ecommerce/SamECommProject'

export default [
	{ path: '', component: Portfolio },
	{ path: '/portfolio', component: Portfolio },

	{ path: '/portfolio/snotel', component: SnotelProject },

	{ path: '/portfolio/microservices/rideshare', component: RideShareServicesProject },
	{path: '/portfolio/microservices/healthcare', component: HealthCareServicesProject},


	{ path: '/portfolio/serverless/ecommerce', component: SamECommProject },
]
