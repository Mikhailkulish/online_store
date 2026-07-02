class PrintMixin:
    """Класс-миксин для печати информации о создании объекта"""

    def __init__(self, *args, **kwargs):
        """Сохраняем параметры для использования в __repr__"""
        self._args = args
        self._kwargs = kwargs
        super().__init__(*args, **kwargs)

        print(repr(self))

    def __repr__(self):
        """Магический метод для строкового представления объекта"""
        class_name = self.__class__.__name__

        # Формируем параметры из сохраненных args и kwargs
        params = []
        for arg in self._args:
            params.append(repr(arg))
        for key, value in self._kwargs.items():
            params.append(f"{key}={repr(value)}")

        return f"{class_name}({', '.join(params)})"
