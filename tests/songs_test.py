

def test_csv_upload(client, auth):
    reg = auth.register()
    log = auth.login()
    csv = "tests/music.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "music.csv")}
    post = client.post("/songs/upload", data=data)

    print(post.data)

    assert post.status_code == 302
    assert post.headers["Location"] == "/songs"