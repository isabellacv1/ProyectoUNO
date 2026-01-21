from users.models import User
from services.models import ServiceRequest

def get_available_technician():
    technicians = User.objects.filter(user_type='technician')

    for tech in technicians:
        busy = ServiceRequest.objects.filter(
            technician=tech,
            status__in=['assigned', 'in_progress']
        ).exists()

        if not busy:
            return tech

    return None
