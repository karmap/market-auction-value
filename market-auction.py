import json
import sys

INPUT_JSON_FILENAME = 'api-response.json'

def calc_market_auction(model, year, data):
    model_data = None
    cost = None

    try:
        model_data = data[model]
        cost = data[model]['saleDetails']['cost']
    except KeyError:
        print("Error: Wrong Model ID")
        return

    try:
        market_ratio  = model_data['schedule']['years'][year]['marketRatio']
        auction_ratio = model_data['schedule']['years'][year]['auctionRatio']
        return {
            'Market':  cost * market_ratio,
            'Auction': cost * auction_ratio
        }
    except KeyError:
        # Calculate Year with no data
        first_year = list(model_data['schedule']['years'].keys())[0]
        last_year = list(model_data['schedule']['years'].keys())[-1]
        default_market_ratio = model_data['schedule']['defaultMarketRatio']
        default_auction_ratio = model_data['schedule']['defaultAuctionRatio']

        if year > last_year:
            years_diff = int(year) - int(last_year)
            market_ratio  = float(model_data['schedule']['years'][last_year]['marketRatio'])
            auction_ratio = float(model_data['schedule']['years'][last_year]['auctionRatio'])
            calc_market_ratio  = (default_market_ratio  + 1) ** years_diff * market_ratio
            calc_auction_ratio = (default_auction_ratio + 1) ** years_diff * auction_ratio
        else:
            years_diff = int(first_year) - int(year)
            market_ratio  = float(model_data['schedule']['years'][first_year]['marketRatio'])
            auction_ratio = float(model_data['schedule']['years'][first_year]['auctionRatio'])
            calc_market_ratio  = (1 - default_market_ratio ) ** years_diff * market_ratio
            calc_auction_ratio = (1 - default_auction_ratio) ** years_diff * auction_ratio
        
        return {
            'Market':  cost * calc_market_ratio,
            'Auction': cost * calc_auction_ratio
        }


def load_input_json(filename):
    with open(filename, "r") as read_file:
        try:
            return json.load(read_file)
        except:
            print("Error reading JSON input file")
            return False

if __name__ == '__main__':
    data = load_input_json(INPUT_JSON_FILENAME)
    # print(calc_market_auction("67352", "2007", data))
    # print(calc_market_auction("87964", "2011", data))

    print(calc_market_auction(sys.argv[1], sys.argv[2], data))