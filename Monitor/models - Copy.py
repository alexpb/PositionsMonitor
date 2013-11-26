from django.db import models

# Create your models here.

class TradeFund(models.Model):
    trade_fund_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    folder = models.CharField(max_length=256)
    active = models.BooleanField(default = True)
    holding_period = models.IntegerField()
    """broker_account_id` int(10) unsigned NOT NULL,
    `media_source_id` int(10) unsigned NOT NULL,
    `responsible_persons_emails` varchar(256) NOT NULL,
    `use_hedging` tinyint(1) NOT NULL,
    `sale_attestation_required` tinyint(1) DEFAULT '0',
    `base_capital_part` decimal(12,4) NOT NULL DEFAULT '1.0000',
    `gearing` decimal(12,4) NOT NULL,
    `daily_ratio` decimal(12,4) NOT NULL DEFAULT '1.0000',
    `max_position_size_in_percentage` decimal(12,4) DEFAULT NULL,
    `max_position_size_in_money` decimal(12,4) DEFAULT NULL,
    `equity_enter_order_type_id` int(10) unsigned NOT NULL DEFAULT '2',
    `equity_enter_order_lifetime_in_seconds` int(11) NOT NULL DEFAULT '420',
    `equity_exit_order_type_id` int(10) NOT NULL,
    `equity_exit_order_validity_from_offset` int(11) DEFAULT NULL,
    `hedge_enter_order_type_id` int(10) unsigned NOT NULL DEFAULT '1',
    `hedge_enter_order_lifetime_in_seconds` int(11) DEFAULT NULL,
    `hedge_exit_order_type_id` int(10) NOT NULL,
    `hedge_exit_order_validity_from_offset` int(11) DEFAULT NULL,
    `max_allowed_order_amount` decimal(12,4) NOT NULL,
    `max_allowed_hedge_order_amount` decimal(12,4) NOT NULL,
    `min_allowed_hedge_order_amount` decimal(12,4) DEFAULT NULL,
    `max_hedge_shares_per_balancing_run` int(11) NOT NULL,
    `avoid_earning_announcement` tinyint(1) NOT NULL DEFAULT '1',
    `days_before_earning_announcement` int(11) NOT NULL DEFAULT '1',
    `days_after_earning_announcement` int(11) NOT NULL DEFAULT '5',
    `exit_on_earning_announcement` tinyint(1) NOT NULL,
    `embargo_schema_id` int(11) NOT NULL DEFAULT '1',
    `avoid_corporate_actions` tinyint(1) NOT NULL DEFAULT '1',
    `avoid_missing_hedge_corporate_actions` tinyint(1) NOT NULL DEFAULT '0',
    `minimum_share_price` decimal(12,4) NOT NULL DEFAULT '5.0000',
    `destination_route` varchar(32) NOT NULL,
    `hedge_destination_route` varchar(32) NOT NULL,
    `minimum_market_capital` decimal(20,6) DEFAULT NULL,
    `require_etfs_easy_to_borrow_check` tinyint(1) NOT NULL DEFAULT '0',
    """

    class Meta:
        db_table = 'trade_fund'

class Holding(models.Model):
    holding_id = models.IntegerField(primary_key=True)
    trade_fund = models.ForeignKey(TradeFund)
    #order = models.ForeignKey(Order)
    ticker = models.CharField(max_length=10, db_index=True)
    quantity = models.IntegerField()
    #trade_type = models.ForeignKey(TradeType)
    buying_price = models.DecimalField(max_digits=12, decimal_places=4)
    buying_date = models.DateTimeField()

    class Meta:
        db_table = 'holding'
