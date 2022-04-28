
def test_csv_upload(client, auth):
    reg = auth.register()
    log = auth.login()
    csv = "tests/music.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "test_music.csv")}
    post = client.post("/songs", data=data)

    print(post.data)

    assert post.status_code == 302
    assert post.headers["Location"] == "/songs_tables"