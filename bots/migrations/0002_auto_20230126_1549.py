# Generated by Django 3.2.7 on 2023-01-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LiquidityMatch',
        ),
        migrations.DeleteModel(
            name='LiquidityStat',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='binance_api_key',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='binance_secret_key',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='liquidity_buy_order_size',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='liquidity_min_btc_balance',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='liquidity_min_eth_balance',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='liquidity_min_usdt_balance',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='liquidity_order_step',
        ),
        migrations.RemoveField(
            model_name='botconfig',
            name='liquidity_sell_order_size',
        ),
        migrations.AlterField(
            model_name='botconfig',
            name='strategy',
            field=models.CharField(choices=[('trade_draw_graph', 'Draw graph')], default='trade_draw_graph', max_length=255),
        ),
    ]
