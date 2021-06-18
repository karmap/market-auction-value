import json

INPUT_JSON_FILENAME = 'api-response.json'

def calc_market_auction(model, year, data):
    try:
        cost = data[model]['saleDetails']['cost']
        market_ratio  = data[model]['schedule']['years'][year]['marketRatio']
        auction_ratio = data[model]['schedule']['years'][year]['auctionRatio']
        # print(cost, market_ratio, auction_ratio)
        return {
            'Market':  cost * market_ratio,
            'Auction': cost * auction_ratio
        }
    except KeyError:
        print("Error: Wrong Model ID or no Year data")
        return
    except:
        print("Error: calculating MarketValue and AuctionValue")
        return

def load_input_json(filename):
    with open(filename, "r") as read_file:
        try:
            return json.load(read_file)
        except:
            print("Error reading JSON input file")
            return False

if __name__ == '__main__':
    data = load_input_json(INPUT_JSON_FILENAME)
    print(calc_market_auction("67352", "2007", data))
    print(calc_market_auction("87964", "2011", data))
