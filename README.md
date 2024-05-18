# Порівняльний аналіз ефективності ефективність жадібного алгоритму та алгоритму динамічного програмування для вирішення задачі про розбиття суми на монети

## Підготовчий етап

- Створенная функцій для жадібного алгоритму, динамічного алгоритму шляхом знизу до гори і згори до низу засобами Python

- Створення допоміжних функцій для генерації даних та заміру часу роботи алгоритмів в мілісекундах

## Опис

Для порівняння 4 функій: вирішення за допомогою жадібного алгоритму, та 3 імплементацій жадібного алгоритму: способом знизу до гори, згори до низу з мемоїзацією за допомогою словника і з мемоізацією за допомогою кешу за часом виконання протестуємо алгоритми на однакових наборах:

- наближених до реальності, де монетами видають 10 000 разів випадково згенеровані суми в межах 100
- на великих сумах випадково згенерованих від 1000 до 1100 для 100 випадків
- на великих сумах випадково згенерованих від 1000 до 1100 для 10000 випадків (без мемоізації словником - виключений, як занадто повільний)

Проведемо заміри часу виконання використовуючи модуль timeit, розрахуємо середнє значення та відобразумо у мілісекундах для зручності.

## Емпірічні результати

Середні часи виконання функцій для 10 000 випадкових сум з amount у межах 100:

| Function                 | Average Time |
| ------------------------ | ------------ |
| find_coins_greedy        | 0.001343     |
| find_min_coins_lru_cache | 0.000633     |
| find_min_coins_bottom_up | 0.020344     |
| find_min_coins_memo      | 0.964728     |

Середні часи виконання функцій для 100 випадкових великих сум з amount у межах 1000-1100:

| Function                 | Average Time |
| ------------------------ | ------------ |
| find_coins_greedy        | 0.003153     |
| find_min_coins_lru_cache | 0.321778     |
| find_min_coins_bottom_up | 0.577825     |
| find_min_coins_memo      | 29.816102    |

Середні часи виконання функцій для 10 000 випадкових великих сум з amount у межах 1000-1100:

| Function                 | Average Time |
| ------------------------ | ------------ |
| find_coins_greedy        | 0.003175     |
| find_min_coins_lru_cache | 0.003689     |
| find_min_coins_bottom_up | 0.568960     |

## Висновки

Розрахунки показують, що для даних наближений до реальності використання касового апарату, де решта розраховується в межах суми 100 найкращі результати показує алгортм динамічного програмування з мемоїзацією реалізованою за допомогою кешу пайтон, на другому місці жадібний алгоритм, наступна реалізація - динамічне програмування знизу до гори, разюче гірше показує себе мемоїзація імплементована вручну. Тож для подібної ситуації, на мою думку найкраще обрати алгоритм динамічного програмування з використання кешу.

Розрахунки для великих сум на 100 симуляціяї показують, що жадібний алгоритм демоснтрує набагато більшу ефективність за інші алгоритми, на другому місці знаходиться реалізація з застосуванням кешу, найгірше показує, як і в першому випадку алгоритм з мемоїзацією з використання словника. Тож для випадків з великими сумами - у разі якщо припустимий вибір ненайоптимальнішого рішення можна обрати жадібний алгоритм, як найбільш ефективний, або ж коли вибір оптимального рішення є критичним - надати перевагу імплементації динамічного програмування з кешем

Водночас розрахунки для великих сум на 10 000 симуляціях показують, що вже на цій кількості алгоритм динамічного програмування з кешем майже зрівнюється з показниками жадібного алгоритму.

Тож вибір між двома найбільш ефективними алгоритмами: жадібним чи динамічним з кешем залежить від умов і обмежень використання

## Передумова

Встановити модуль pandas

```
pip install pandas
```
