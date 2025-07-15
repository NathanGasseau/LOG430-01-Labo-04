from prometheus_client import Counter
from django.utils.deprecation import MiddlewareMixin

http_requests_total = Counter(
    'http_requests_total_by_status',
    'Nombre total de requêtes HTTP par code de statut',
    ['method', 'status']
)

class MetricsMiddleware(MiddlewareMixin):
    def __call__(self, request):
        response = self.get_response(request)

        # Ajoute une entrée dans le compteur
        http_requests_total.labels(method=request.method, status=response.status_code).inc()

        return response
