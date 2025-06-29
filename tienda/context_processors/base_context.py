from tienda.models import Cliente

def base_context(request):
    cliente_id = request.session.get('cliente_id')
    es_admin = False
    if cliente_id:
        cliente = Cliente.objects.filter(id=cliente_id).first()
        if cliente and cliente.is_admin:
            es_admin = True
    return {'es_admin': es_admin}
