
console.log('Hello from service-worker.js');

importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js');

// This will listen for messages of type: 'SKIP_WAITING' and run the skipWaiting() method, forcing the service worker to
// activate right away.
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        console.log("Invoked skipWaiting");
        self.skipWaiting();
    }
});

// Check if workbox loaded
if (workbox) {
    console.log("Workbox is loaded.");
} else {
    console.log("Workbox didn't load");
}

// workbox.setConfig({debug: true});

// This will trigger the importScripts() for workbox.strategies, routing etc and their dependencies:
const {strategies} = workbox;
const {routing} = workbox;
const {precaching} = workbox;
const {core} = workbox;
const cacheable_response = workbox.cacheableResponse;
const expiration = workbox.expiration;
// const {navigtaionPreload} = workbox;

//import {cacheNames} from 'workbox-core';
//const precacheCacheName = cacheNames.precache;
//const runtimeCacheName = cacheNames.runtime;
//const googleAnalyticsCacheName = cacheNames.googleAnalytics;
//import {setCacheNameDetails} from 'workbox-core';

core.setCacheNameDetails({
    prefix: 'airport_finder',
    suffix: 'v1',
    precache: 'precache',
    runtime: 'runtime',
    googleAnalytics: 'analytics'
});


// Cache CSS and javaScript assets with a stale-while-revalidate strategy.
routing.registerRoute(
    ({request}) => request.destination === 'script' ||
        request.destination === 'style',
    new strategies.StaleWhileRevalidate({
        cacheName: 'static-resources',
    })
);

// Cache image files with a cache-first strategy for 30 days.
routing.registerRoute(
    ({request}) => request.destination === 'image',
    new strategies.CacheFirst({
        cacheName: 'images',
        plugins: [
            new expiration.ExpirationPlugin({
                maxEntries: 60,
                maxAgeSeconds: 30 * 24 * 60 * 60,
            }),
        ],
    })
);

//google fonts
//import {registerRoute} from 'workbox-routing';
//import {CacheFirst, StaleWhileRevalidate} from 'workbox-strategies';
//import {CacheableResponsePlugin} from 'workbox-cacheable-response';
//import {ExpirationPlugin} from 'workbox-expiration';

// Cache the Google Fonts stylesheets with a stale-while-revalidate strategy.
routing.registerRoute(
  ({url}) => url.origin === 'https://fonts.googleapis.com',
  new strategies.StaleWhileRevalidate({
    cacheName: 'google-fonts-stylesheets',
  })
);

// Cache the underlying font files with a cache-first strategy for 1 year.
routing.registerRoute(
  ({url}) => url.origin === 'https://fonts.gstatic.com',
  new strategies.CacheFirst({
    cacheName: 'google-fonts-webfonts',
    plugins: [
      new cacheable_response.CacheableResponsePlugin({
        statuses: [0, 200],
      }),
      new expiration.ExpirationPlugin({
        maxAgeSeconds: 60 * 60 * 24 * 365,
        maxEntries: 30,
      }),
    ],
  })
);


//static files
routing.registerRoute(
  ({url}) => url.origin === self.location.origin &&
             url.pathname.startsWith('/static/'),
  new strategies.StaleWhileRevalidate()
);