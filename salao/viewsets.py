from rest_framework import viewsets, permissions
from .models import Salao
from .serializers import SalaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class SalaoViewSet(viewsets.ModelViewSet):
    """
    /api/salao/           -> GET (lista) / POST (cria)
    /api/salao/<id>/      -> GET / PUT / PATCH / DELETE
    """
    serializer_class = SalaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # retorna todos os salões cadastrados
        return Salao.objects.all()

    def perform_create(self, serializer):
        # o salão criado pertence ao usuário logado
        serializer.save()


    # ROTA PERSONALIZADA PARA LISTAR TODOS OS SALÕES
    @action(detail=False, methods=['get'], url_path='todos')
    def listar_todos(self, request):
        saloes = Salao.objects.all()
        serializer = self.get_serializer(saloes, many=True)
        return Response(serializer.data)
    

    # ROTA: /api/salao/<id>/servicos/
    @action(detail=True, methods=['get'], url_path='servicos')
    def listar_servicos_salao(self, request, pk=None):
        try:
            salao = Salao.objects.get(pk=pk)
        except Salao.DoesNotExist:
            return Response({"detail": "Salão não encontrado."}, status=404)

        from servico.serializers import ServicoSerializer
        servicos = salao.servicos.all()  # pelo related_name="servicos"
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)



# O serializer já associa o salão ao usuário automaticamente.
# Por isso, não passamos "usuario" no perform_create().
# perform_create() apenas chama serializer.save() sem parâmetros.



