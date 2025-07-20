import requests,os,zipfile,shutil

GITHUB_REPO_URL = "https://github.com/haxer19/C-u-C-"
RAW_VERSION_URL = "https://raw.githubusercontent.com/haxer19/C-u-C-/main/version.txt"
ZIP_URL = "https://github.com/haxer19/C-u-C-/archive/refs/heads/main.zip"

LOCAL_VERSION_FILE = "version.txt"

def _check_v_():
    if not os.path.exists(LOCAL_VERSION_FILE):
        return "0.0.0"
    with open(LOCAL_VERSION_FILE, "r") as f:
        return f.read().strip()

def _get_v_():
    try:
        response = requests.get(RAW_VERSION_URL)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return None
    except:
        return None

def _rs_t_():
    print("Đang tải bản cập nhật...")
    r = requests.get(ZIP_URL)
    with open("update.zip", "wb") as f:
        f.write(r.content)

    with zipfile.ZipFile("update.zip", 'r') as zip_ref:
        zip_ref.extractall("update_temp")
        
    _srcF_ = os.path.join("update_temp", os.listdir("update_temp")[0])
    for item in os.listdir(_srcF_):
        if item != "updater.py":
            s = os.path.join(_srcF_, item)
            d = os.path.join(".", item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

    shutil.rmtree("update_temp")
    os.remove("update.zip")
    print("Đã cập nhật thành công!")

def _check_update_():
    local = _check_v_()
    remote = _get_v_()
    print(f"Phiên bản hiện tại: {local} | Phiên bản trên GitHub: {remote}")
    if remote and remote != local:
        choice = input("Có bản cập nhật mới. Bạn có muốn cập nhật? (Y/N): ").lower()
        if choice == 'y':
            _rs_t_()
            print("Vui lòng khởi động lại chương trình.")
            exit()
    else:
        print("Bạn đang dùng phiên bản mới nhất.")
