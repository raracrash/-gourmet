#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ホットペッパーグルメAPI プロキシサーバー
Render対応版
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request
import urllib.parse
import json
import os
from urllib.error import URLError, HTTPError

class ProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # /api/hotpepper へのリクエストをプロキシ
        if self.path.startswith('/api/hotpepper'):
            self.proxy_hotpepper_api()
        else:
            # 通常のファイル配信
            super().do_GET()
    
    def proxy_hotpepper_api(self):
        try:
            # クエリパラメータを取得
            parsed_path = urllib.parse.urlparse(self.path)
            query_params = urllib.parse.parse_qs(parsed_path.query)
            
            # ホットペッパーAPIのURL構築
            hotpepper_base_url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
            
            # パラメータを再構築（format=jsonに固定）
            api_params = {}
            for key, value in query_params.items():
                api_params[key] = value[0]
            
            # format を json に設定
            api_params['format'] = 'json'
            
            # URLエンコード
            encoded_params = urllib.parse.urlencode(api_params)
            full_url = f"{hotpepper_base_url}?{encoded_params}"
            
            print(f"リクエスト: {full_url}")
            
            # APIを呼び出し
            with urllib.request.urlopen(full_url) as response:
                data = response.read()
                
                # CORSヘッダーを設定してレスポンス
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.end_headers()
                
                self.wfile.write(data)
                
        except HTTPError as e:
            print(f"HTTPエラー: {e.code} - {e.reason}")
            self.send_error(e.code, f"API Error: {e.reason}")
        except URLError as e:
            print(f"URLエラー: {e.reason}")
            self.send_error(500, f"API Error: {e.reason}")
        except Exception as e:
            print(f"予期しないエラー: {str(e)}")
            self.send_error(500, f"Internal Error: {str(e)}")
    
    def do_OPTIONS(self):
        # プリフライトリクエストに対応
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server(port=8000):
    server_address = ('0.0.0.0', port)  # Render用に0.0.0.0にバインド
    httpd = HTTPServer(server_address, ProxyHandler)
    print(f"")
    print(f"🍴 グルメファインダー サーバー起動")
    print(f"=" * 50)
    print(f"サーバーアドレス: http://0.0.0.0:{port}")
    print(f"=" * 50)
    print(f"サーバーを停止するには Ctrl+C を押してください")
    print(f"")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n\nサーバーを停止しています...")
        httpd.shutdown()
        print(f"サーバーを停止しました")

if __name__ == '__main__':
    # Renderの環境変数からポート番号を取得（デフォルトは8000）
    port = int(os.environ.get('PORT', 8000))
    run_server(port)
