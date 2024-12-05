<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <h1>Tank Game Project</h1>
    <div class="section">
        <h2>Giới thiệu</h2>
        <p>Đây là một dự án game bắn xe tank được phát triển dựa trên ý tưởng trò chơi nổi tiếng <strong>Tank Trouble</strong>. Game đã được xây dựng thêm các tính năng độc đáo, bao gồm:</p>
        <ul>
            <li><strong>Đạn đuổi tên lửa:</strong> Tự động tìm kiếm và bám đuổi mục tiêu.</li>
            <li><strong>Đạn Lazer Beam:</strong> Bắn tia laser mạnh mẽ gây sát thương lớn.</li>
        </ul>
        <p>Game được phát triển bằng Python với các thư viện <strong>pygame</strong>, <strong>tkinter</strong>, và tích hợp thêm C++ với thư viện <strong>GLFW</strong>.</p>
    </div>
    <div class="section">
        <h2>Cách chạy chương trình</h2>
        <h3>Phương pháp 1: Chạy bằng file thực thi</h3>
        <p>Thực hiện các bước sau:</p>
        <ul>
            <li>Mở thư mục <strong>Setting</strong>.</li>
            <li>Tìm file có tên <strong>setting.exe</strong>.</li>
            <li>Nhấp vào file này và chạy chương trình.</li>
        </ul>
        <h3>Phương pháp 2: Chạy bằng mã nguồn</h3>
        <p>Thực hiện các bước sau:</p>
        <ul>
            <li>Vào thư mục chính của game.</li>
            <li>Tìm file <strong>main.py</strong>.</li>
            <li>Trong file <strong>main.py</strong>, hãy <strong>bình luận (comment)</strong> hoặc <strong>xóa</strong> dòng:
                <pre><code>subprocess.run(["mid.exe"])</code></pre>
            </li>
            <li>Chạy file <strong>main.py</strong> như bình thường. Lưu ý đây chỉ là file chính của game.</li>
            <li>Để chạy phần cài đặt (settings), hãy vào thư mục <strong>Setting</strong>, tìm file <strong>setting.py</strong> và chạy file này.</li>
        </ul>
    </div>
    <div class="section">
        <h2>Thư viện cần thiết</h2>
        <p>Để chạy được mã nguồn, bạn cần cài đặt các thư viện sau:</p>
        <ul>
            <li><strong>tkinter</strong></li>
            <li><strong>pygame</strong></li>
            <li><strong>numpy</strong></li>
        </ul>
    </div>
</body>
</html>
