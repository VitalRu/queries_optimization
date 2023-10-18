### Архитектура

1. Сущность продукта. У продукта есть владелец. Есть сущность для сохранения доступов к продукту для пользователя.
2. Сущность урока. Урок может находиться в нескольких продуктах одновременно. В уроке базовая информация: название, ссылка на видео, длительность просмотра (в секундах).
3. Урок могут просматривать множество пользователей. Для каждого фиксируется время просмотра и статус “Просмотрено”/”Не просмотрено”. Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.

### Запросы

1. API для выведения списка всех уроков по всем продуктам к которым пользователь имеет доступ, с выведением информации о статусе и времени просмотра.
2. API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ, с выведением информации о статусе и времени просмотра, а также датой последнего просмотра ролика.
3. API для отображения статистики по продуктам. Отображение списка всех продуктов на платформе, к каждому продукту приложена информация:
    - Количество просмотренных уроков от всех учеников.
    - Сколько в сумме все ученики потратили времени на просмотр роликов.
    - Количество учеников занимающихся на продукте.
    - Процент приобретения продукта (рассчитывается исходя из количества полученных доступов к продукту деленное на общее количество пользователей на платформе).
