# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from metafab_python.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from metafab_python.model.auth_game200_response import AuthGame200Response
from metafab_python.model.auth_game200_response_all_of import AuthGame200ResponseAllOf
from metafab_python.model.auth_game200_response_all_of1 import AuthGame200ResponseAllOf1
from metafab_python.model.auth_player200_response import AuthPlayer200Response
from metafab_python.model.batch_mint_collection_items_request import BatchMintCollectionItemsRequest
from metafab_python.model.batch_transfer_collection_items_request import BatchTransferCollectionItemsRequest
from metafab_python.model.batch_transfer_currency_request import BatchTransferCurrencyRequest
from metafab_python.model.burn_collection_item_request import BurnCollectionItemRequest
from metafab_python.model.burn_currency_request import BurnCurrencyRequest
from metafab_python.model.collection_model import CollectionModel
from metafab_python.model.contract_model import ContractModel
from metafab_python.model.create_collection200_response import CreateCollection200Response
from metafab_python.model.create_collection200_response_all_of import CreateCollection200ResponseAllOf
from metafab_python.model.create_collection200_response_all_of_contract import CreateCollection200ResponseAllOfContract
from metafab_python.model.create_collection200_response_all_of_contract_all_of import CreateCollection200ResponseAllOfContractAllOf
from metafab_python.model.create_collection_item_request import CreateCollectionItemRequest
from metafab_python.model.create_collection_item_request_attributes_inner import CreateCollectionItemRequestAttributesInner
from metafab_python.model.create_collection_request import CreateCollectionRequest
from metafab_python.model.create_contract_request import CreateContractRequest
from metafab_python.model.create_currency200_response import CreateCurrency200Response
from metafab_python.model.create_currency_request import CreateCurrencyRequest
from metafab_python.model.create_game_request import CreateGameRequest
from metafab_python.model.create_player_request import CreatePlayerRequest
from metafab_python.model.currency_model import CurrencyModel
from metafab_python.model.game_model import GameModel
from metafab_python.model.get_collections200_response_inner import GetCollections200ResponseInner
from metafab_python.model.get_collections200_response_inner_all_of import GetCollections200ResponseInnerAllOf
from metafab_python.model.get_currencies200_response_inner import GetCurrencies200ResponseInner
from metafab_python.model.get_currencies200_response_inner_all_of import GetCurrencies200ResponseInnerAllOf
from metafab_python.model.get_currency_fees200_response import GetCurrencyFees200Response
from metafab_python.model.mint_collection_item_request import MintCollectionItemRequest
from metafab_python.model.mint_currency_request import MintCurrencyRequest
from metafab_python.model.player_model import PlayerModel
from metafab_python.model.set_collection_approval_request import SetCollectionApprovalRequest
from metafab_python.model.set_collection_item_timelock_request import SetCollectionItemTimelockRequest
from metafab_python.model.set_currency_fees_request import SetCurrencyFeesRequest
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.transfer_collection_item_request import TransferCollectionItemRequest
from metafab_python.model.transfer_currency_request import TransferCurrencyRequest
from metafab_python.model.update_game_request import UpdateGameRequest
from metafab_python.model.update_player_request import UpdatePlayerRequest
from metafab_python.model.wallet_model import WalletModel
from metafab_python.model.write_contract_request import WriteContractRequest
