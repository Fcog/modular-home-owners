from mhoapp.base.models import MHOSettings


def global_data(request):
    # Fixed data structures to pass to all templates
    return {
        'mhoapp': MHOSettings.objects.first(),
    }