# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class BrokerAccount(models.Model):
    broker_account_id = models.IntegerField(primary_key=True)
    stock_exchange_broker = models.ForeignKey('StockExchangeBroker')
    broker_account_group = models.ForeignKey('BrokerAccountGroup')
    account = models.CharField(unique=True, max_length=32)
    class Meta:
        managed = False
        db_table = 'broker_account'

class BrokerAccountGroup(models.Model):
    broker_account_group_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64, blank=True)
    easy_to_borrow_source = models.ForeignKey('EasyToBorrowSource', blank=True, null=True)
    require_short_validation = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'broker_account_group'

class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    ticker = models.CharField(unique=True, max_length=16)
    name = models.CharField(max_length=256, blank=True)
    financial_instrument_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'company'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class EasyToBorrow(models.Model):
    ticker = models.CharField(max_length=16)
    quantity = models.IntegerField(blank=True, null=True)
    date_inserted = models.DateTimeField(blank=True, null=True)
    broker_account_group = models.ForeignKey(BrokerAccountGroup)
    class Meta:
        managed = False
        db_table = 'easy_to_borrow'

class EasyToBorrowSource(models.Model):
    easy_to_borrow_source_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64, blank=True)
    class Meta:
        managed = False
        db_table = 'easy_to_borrow_source'

class Hedge(models.Model):
    hedge_id = models.IntegerField(primary_key=True)
    ticker = models.CharField(unique=True, max_length=8)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    financial_instrument_id = models.IntegerField(unique=True)
    class Meta:
        managed = False
        db_table = 'hedge'

class Holding(models.Model):
    holding_id = models.IntegerField(primary_key=True)
    trade_fund = models.ForeignKey('TradeFund')
    order = models.ForeignKey('Order', blank=True, null=True)
    ticker = models.CharField(max_length=16)
    quantity = models.IntegerField()
    trade_type = models.ForeignKey('TradeType')
    buying_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    buying_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'holding'

class MediaSource(models.Model):
    media_source_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'media_source'

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    parent_signal = models.ForeignKey('Signal', blank=True, null=True)
    trade_fund = models.ForeignKey('TradeFund')
    ie_order_id = models.BigIntegerField(blank=True, null=True)
    order_side = models.ForeignKey('OrderSide')
    ticker = models.CharField(max_length=16)
    shares = models.IntegerField(blank=True, null=True)
    order_type = models.ForeignKey('OrderType', blank=True, null=True)
    limit = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_offset = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hedge_ticker = models.CharField(max_length=16, blank=True)
    hedge_shares = models.IntegerField(blank=True, null=True)
    order_time_in_force = models.ForeignKey('TimeInForce', blank=True, null=True)
    good_after_date = models.DateTimeField(blank=True, null=True)
    good_until_date = models.DateTimeField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    milliseconds_submitted = models.IntegerField(blank=True, null=True)
    client_order_id = models.CharField(unique=True, max_length=32, blank=True)
    broker_order_id = models.CharField(max_length=32, blank=True)
    shares_filled = models.IntegerField(blank=True, null=True)
    execution_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    date_executed = models.DateTimeField(blank=True, null=True)
    order_status = models.ForeignKey('OrderStatus')
    broker_order_status = models.CharField(max_length=32, blank=True)
    position_type = models.ForeignKey('PositionType')
    is_hedge_order = models.IntegerField()
    date_created = models.DateTimeField()
    beta = models.DecimalField(max_digits=12, decimal_places=4)
    destination_exchange = models.CharField(max_length=32, blank=True)
    awaiting_correction = models.IntegerField()
    max_participation = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    aggression = models.IntegerField(blank=True, null=True)
    participate_on_open = models.IntegerField()
    participate_on_close = models.IntegerField()
    tracking = models.IntegerField(blank=True, null=True)
    post_quantity = models.IntegerField(blank=True, null=True)
    refill_quantity = models.IntegerField(blank=True, null=True)
    algo_order_type_id = models.IntegerField(blank=True, null=True)
    routing_instructions = models.CharField(max_length=32, blank=True)
    class Meta:
        managed = False
        db_table = 'order'

class OrderSide(models.Model):
    order_order_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'order_side'

class OrderStatus(models.Model):
    order_status_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    is_final = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'order_status'

class OrderType(models.Model):
    order_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'order_type'

class PositionType(models.Model):
    position_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'position_type'

class Signal(models.Model):
    signal_id = models.IntegerField(primary_key=True)
    trade_fund = models.ForeignKey('TradeFund')
    ie_order_id = models.BigIntegerField()
    trade_type = models.ForeignKey('TradeType')
    position_type = models.ForeignKey(PositionType)
    ticker = models.CharField(max_length=16)
    shares = models.IntegerField(blank=True, null=True)
    limit = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hedge_ticker = models.CharField(max_length=16, blank=True)
    hedge_shares = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    beta = models.DecimalField(max_digits=12, decimal_places=4)
    articles_file_start_line = models.IntegerField(blank=True, null=True)
    articles_file_lines_to_read = models.IntegerField(blank=True, null=True)
    articles_inserted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'signal'

class StockExchangeBroker(models.Model):
    stock_exchange_broker_id = models.IntegerField(primary_key=True)
    business_object_key = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'stock_exchange_broker'

class TimeInForce(models.Model):
    time_in_force_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'time_in_force'

class TradeFund(models.Model):
    trade_fund_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    folder = models.CharField(max_length=256)
    active = models.IntegerField()
    holding_period = models.IntegerField(blank=True, null=True)
    broker_account = models.ForeignKey(BrokerAccount)
    media_source = models.ForeignKey(MediaSource)
    responsible_persons_emails = models.CharField(max_length=256)
    use_hedging = models.IntegerField()
    sale_attestation_required = models.IntegerField(blank=True, null=True)
    base_capital_part = models.DecimalField(max_digits=12, decimal_places=4)
    gearing = models.DecimalField(max_digits=12, decimal_places=4)
    daily_ratio = models.DecimalField(max_digits=12, decimal_places=4)
    max_position_size_in_percentage = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_position_size_in_money = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    equity_enter_order_type = models.ForeignKey(OrderType)
    equity_enter_order_lifetime_in_seconds = models.IntegerField()
    equity_exit_order_type_id = models.IntegerField()
    equity_exit_order_validity_from_offset = models.IntegerField(blank=True, null=True)
    hedge_enter_order_type_id = models.IntegerField()
    hedge_enter_order_lifetime_in_seconds = models.IntegerField(blank=True, null=True)
    hedge_exit_order_type_id = models.IntegerField()
    hedge_exit_order_validity_from_offset = models.IntegerField(blank=True, null=True)
    max_allowed_order_amount = models.DecimalField(max_digits=12, decimal_places=4)
    max_allowed_hedge_order_amount = models.DecimalField(max_digits=12, decimal_places=4)
    min_allowed_hedge_order_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_hedge_shares_per_balancing_run = models.IntegerField()
    avoid_earning_announcement = models.IntegerField()
    days_before_earning_announcement = models.IntegerField()
    days_after_earning_announcement = models.IntegerField()
    exit_on_earning_announcement = models.IntegerField()
    embargo_schema_id = models.IntegerField()
    avoid_corporate_actions = models.IntegerField()
    avoid_missing_hedge_corporate_actions = models.IntegerField()
    minimum_share_price = models.DecimalField(max_digits=12, decimal_places=4)
    destination_route = models.CharField(max_length=32)
    hedge_destination_route = models.CharField(max_length=32)
    minimum_market_capital = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    require_etfs_easy_to_borrow_check = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'trade_fund'

class TradeType(models.Model):
    trade_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'trade_type'

