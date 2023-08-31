1. dynamodb_local_latestをダウンロードして、解凍する
2. javaがなければ、インストールする。Pathも通しておく
3. 解凍した階層に行き、java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDbを実行
4. 別のターミナルを開き、venvで仮想環境を作成
5. pip install -r requirements.txtを実行
6. create_table.pyでテーブル作成
7. users_app.pyを実行し、サーバを立てる

※1 table一覧を見たいときは、list_tables.pyを実行
※2 tableを削除したいときは、delete_table.pyを実行