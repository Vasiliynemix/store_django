class TitleMixin:
    title = None

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = self.title
        return context
