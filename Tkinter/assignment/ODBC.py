import pyodbc


class ODBC:
    def __init__(self, driver='SQL Server', server='GROOO0030', database='qlnv', username='', password=''):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self, message=''):
        try:
            config = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
            self.conn = pyodbc.connect(config)
            self.cursor = self.conn.cursor()
            print("Connection successful " + message)
        except Exception as e:
            print("Error in connection: ", e)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(f"An error occurred: {e}")

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return list(self.cursor)

    def employee_Type(self):
        query = "SELECT DISTINCT LoaiNhanVien FROM ChamCongTongHop;"
        self.execute_query(query)
        loai_nhan_vien = self.fetch_all()
        print('employee_Type')
        return loai_nhan_vien

    def list_of_Employee(self):

        query = """SELECT NhanVien.MaNhanVien,
                            ChamCongTongHop.LoaiNhanVien,
                            NhanVien.HoTen,
                            NhanVien.LuongCoBan,
                            ChamCongTongHop.SoNgayLam,
                            ChamCongTongHop.SoSanPham,
                            LuongHangThang.LuongHT
                        FROM NhanVien
                        LEFT JOIN ChamCongTongHop
                        ON NhanVien.MaNhanVien = ChamCongTongHop.MaNhanVien
                        LEFT JOIN LuongHangThang
                        ON NhanVien.MaNhanVien = LuongHangThang.MaNhanVien;"""
        self.execute_query(query)
        nhan_vien = self.fetch_all()
        print('Danh sach nhan vien:')
        return nhan_vien

    def save_monthly_salary_Employee(self, nv):
        pass

    def save_monthly_salary(self, dsNV):
        query = """
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'LuongHangThang')
        BEGIN
            CREATE TABLE LuongHangThang (
                MaNhanVien VARCHAR(255) PRIMARY KEY,
                LuongHT DECIMAL(10, 2),
                FOREIGN KEY (MaNhanVien) REFERENCES NhanVien(MaNhanVien)
            );
        END
        """
        self.execute_query(query)

        # loop employee list
        for nv in dsNV:
            luongHT = nv._luongHT

            query = f"""IF EXISTS (SELECT 1 FROM LuongHangThang WHERE MaNhanVien = '{nv._maNV}')
                        BEGIN
                            UPDATE LuongHangThang SET LuongHT = {luongHT} WHERE MaNhanVien = '{nv._maNV}';
                        END
                        ELSE
                        BEGIN
                            INSERT INTO LuongHangThang (MaNhanVien, LuongHT) VALUES ('{nv._maNV}', {luongHT});
                        END"""
            self.execute_query(query)

        # Commit the changes
        self.conn.commit()

    def add_employee(self, nv):
        query = f"""INSERT INTO NhanVien (MaNhanVien, HoTen, LuongCoBan)
                    VALUES ('{nv._maNV}', '{nv._hoTen}', {nv._luongCB});"""
        self.execute_query(query)

        query = f"""INSERT INTO ChamCongTongHop (MaNhanVien, LoaiNhanVien, SoNgayLam, SoSanPham)
                    VALUES ('{nv._maNV}', '{nv._loaiNV}', {0}, {0});"""
        self.execute_query(query)

        query = f"""INSERT INTO LuongHangThang (MaNhanVien,LuongHT )
                          VALUES ('{nv._maNV}', {0});"""
        self.execute_query(query)

        # Commit the changes
        self.conn.commit()
        print('Đã thêm nhân viên thành công.')
