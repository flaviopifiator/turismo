var staticCacheName = 'turismo-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '',
        '/',
        'calendario/',
        'proveedor/',
        'feedback/clientes/',
        'feedback/proveedores/',
        'static/font/font-awesome-4.7.0/css/font-awesome.min.css',
        'static/css/bootstrap/bootstrap.min.css',
        'static/css/mdb.min.css',
        'static/css/style.css',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '')) {
        event.respondWith(caches.match(''));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});