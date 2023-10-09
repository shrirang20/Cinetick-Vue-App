import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/Home.vue'
import AdminHome from './components/AdminDashboard.vue'
import EditShows from './components/Edit.vue'
import LandingPage from './components/LandingPage.vue'
import EditTheatre from './components/TheatreEdit.vue'
const routes=[
    {
        name:'Home',
        component: HomePage,
        path:'/'
    },
    {
        name:'LandingPage',
        component: LandingPage,
        path:'/bookshow',
    },
    {
        name:'AdminHome',
        component: AdminHome,
        path:'/adminhome',
        
    },
    {
        name:'EditShows',
        component: EditShows,
        path:'/update/:id',
       
    },
    
    {
        name:'EditTheatre',
        component: EditTheatre,
        path:'/update-theatre/:theatrename',
       
    },


]
const router=createRouter({
    history:createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    try {
        const isAdmin = localStorage.getItem('isAdmin') === 'true';
        const isUser = localStorage.getItem('isUser') === 'true';

        if (!isAdmin && !isUser) {
            // No user is logged in, allow access to HomePage and LandingPage only
            if (to.name === 'Home') {
                next();
            } else {
                // Redirect to HomePage
                next({ name: 'Home' });
            }
        } else if (isAdmin) {
            // Admin is logged in, allow access to all routes
            if (to.name === 'AdminHome' || to.name === 'EditShows' || to.name === 'EditTheatre' || to.name === 'Home') {
                next();
            } else {
                // Redirect to AdminHome or other admin pages
                next({ name: 'AdminHome' });
            }
        } else if (isUser) {
            // Regular user is logged in, restrict access to LandingPage
            if (to.name === 'LandingPage') {
                next();
            } else {
                // Redirect to LandingPage
                next({ name: 'LandingPage' });
            }
        }
    } catch (error) {
        console.error('error');
    }
});

export default router



// Check if the route requires admin access
    // if (to.meta.requiresAdmin) {
    
    //     // Check if the user is logged in as an admin
    //     // const isAdmin = localStorage.getItem('isAdmin');
    //     if (isAdmin === 'true') {
    //         // User is an admin, allow access to the route
    //         next();
    //     } else {
    //         // User is not an admin, redirect to the home route or show an error
    //         next('/'); // Redirect to home
    //     }
    // } else if (to.meta.requiresUser) {
    //     // Check if the route requires user access
    //     // const isUser = localStorage.getItem('isUser');
    //     console.log("isUser:",isUser)
    //     if (isUser === 'true') {
    //         // User is a regular user, allow access to the route
    //         next();
    //     } else {
    //         // User is not a regular user, redirect to the home route or show an error
    //         next('/'); // Redirect to home
    //     }
    // } else {
    //     // For routes that don't require admin or user access, proceed to the route
    //     next();
    // }


    // const isAdmin = localStorage.getItem('isAdmin') === 'true';
    //     const isUser = localStorage.getItem('isUser') === 'true';

    //     if (isAdmin && isUser === null) {
    //         // Set them to false (no user logged in)
    //         localStorage.setItem('isAdmin', 'false');
    //         localStorage.setItem('isUser', 'false');
    //     }

    //     if (isAdmin) {
    //         // Admin is logged in, allow access to all routes
    //         next();
    //     } else if (isUser) {
    //         // Regular user is logged in, restrict access to LandingPage
    //         if (to.name === 'LandingPage'|| to.name === 'HomePage') {
    //             next();
    //         } else {
    //             // Redirect to LandingPage
    //             next({ name: 'LandingPage' });
    //         }
    //     } 
    //     else {
    //         // No user is logged in, allow access to HomePage and LandingPage only
    //         if (to.name === 'HomePage') {
    //             next();
    //         } else {
    //             // Redirect to HomePage
    //             next({ name: 'HomePage' });
    //         }
    //     }
    // } catch(error){
    //     console.error('error')
    // }
   