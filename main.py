import csv


def main():
    # レストラン名と選ばれた回数を保存するためのCSVファイルのパス
    csv_file_path = 'ranking.csv'

    print('こんにちは!私はRobokoです。あなたの名前は何ですか?')
    user_name = input()

    # CSVファイルの読み込み
    posted_restaurants = read_csv(csv_file_path)
    if len(posted_restaurants) == 0:
        print(f'{user_name}さん。どこのレストランが好きですか?')
        restaurant_name = input()
        restaurant_name = restaurant_name.capitalize()

        posted_restaurants[restaurant_name] = 1

        write_csv(csv_file_path, posted_restaurants)

        print(f'{user_name}さん、ありがとうございました。\n良い一日を!さようなら')
    else:
        # CSVファイルに複数のレストランが登録されている場合、選ばれた回数でソート
        recommend_restaurants_ranking = sorted(
            posted_restaurants, key=posted_restaurants.get, reverse=True)

        # 選ばれた回数が多いレストランから表示
        for recommend_restaurant in recommend_restaurants_ranking:
            print(
                f'私のオススメのレストランは、{recommend_restaurant}です。\nこのレストランは好きですか？[Yes/No]')
            yes_no_answer = input()
            yes_no_answer = yes_no_answer.lower()
            if yes_no_answer == 'yes':
                break

        print(f'{user_name}さん。どこのレストランが好きですか?')
        restaurant_name = input()
        restaurant_name = restaurant_name.capitalize()

        if restaurant_name in posted_restaurants:
            posted_restaurants[restaurant_name] += 1
        else:
            posted_restaurants[restaurant_name] = 1

        write_csv(csv_file_path, posted_restaurants)

        print(f'{user_name}さん、ありがとうございました。\n良い一日を!さようなら')


def read_csv(csv_file_path):
    posted_restaurants = {}
    with open(csv_file_path, 'r+') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            posted_restaurant_name = row['Name']
            posted_count = row['Count']
            posted_restaurants[posted_restaurant_name] = int(posted_count)
    return posted_restaurants


def write_csv(csv_file_path, restaurants_dict):
    with open(csv_file_path, 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for restaurant_name, count in restaurants_dict.items():
            writer.writerow({'Name': restaurant_name, 'Count': count})


if __name__ == '__main__':
    main()
