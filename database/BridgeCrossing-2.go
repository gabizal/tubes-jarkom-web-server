package main
import "fmt"

// Deklarasi Konstanta
const NMAX int = 5
const USERMAX int = 100
const LAMPLIFE int = 30

// Deklarasi Tipe Bentukan island
type island struct {
	member [NMAX]int
	nMember int
}

// Deklarasi Tipe Bentukan bridge
type bridge struct {
	m1, m2 int
}

// Deklarasi Tipe Bentukan user
type user struct {
	nama string
	time int
}

// Deklarasi Tipe Bentukan users
type users struct {
	info [USERMAX]user
	nUser int
}

func header_1302220072(){
/* I.S. -
   F.S. menampilkan header dari aplikasi */
    fmt.Println()
	fmt.Println("=====Selamat Datang=====")
	fmt.Println("	Bridge Crossing Game	")
	fmt.Println("	Algoritma Pemrograman	")
	fmt.Println("-------------------------")
	fmt.Println("1. Mulai permainan")
	fmt.Println("2. Lihat waktu")
	fmt.Println("3. Keluar")
}

func menu_1302220072(A* users){
/* I.S. terdefinisi tipe bentukan A yang berisi sejumlah A.nUser pemain pada array A.info
   F.S. menampilkan menu permainan, dan array A.info terupdate apabila terdapat pemain baru */
    // a. Buatlah variabel string opsi yang digunakan untuk menyimpan pilihan menu yang dipilih, inisialisasi dengan string kosong
    var opsi string
    // b. Buatlah while dengan kondisi variabel opsi tidak sama dengan string "3" karena pilihan "3" digunakan untuk keluar dari aplikasi
    for opsi != "3" {
        // c. panggil procedure header() yang sudah dibuat. Kemudian tampilkan pilihan opsi 1 hingga 3 sesuai gambar tampilan menu di atas
        header_1302220072()
        fmt.Println("1. Mulai permainan")
		fmt.Println("2. Lihat waktu")
		fmt.Println("3. Keluar")
        fmt.Println(" --------------------------- ")
        // d. Tampilkan string "Pilihan anda: ", kemudian minta masukan untuk variabel opsi
        fmt.Print("Pilihan anda : "); fmt.Scan(&opsi)
        // e. Lakukan perulangan dengan while untuk masukan variabel opsi selama opsi yang diberikan tidak valid (selain 1, 2 dan 3).
        for opsi != "1" && opsi != "2" && opsi != "3" {
            fmt.Scan(&opsi)
        }
        // f. Tambahkan percabangan untuk setiap nilai variabel opsi "1" dan "2" sebelum endwhile. Panggil procedure mulai_permainan(A) untuk opsi "1" dan lihat_skor(*A) untuk opsi "2"
        if opsi == "1" {
            mulai_permainan_1302220072(A)
        }else if opsi == "2" {
            lihat_skor_1302220072(A)
        }
    }
    // g. Setelah endwhile tampilkan string "Terima kasih :)".
    fmt.Println("Terima kasih :)")
}

func lihat_skor_1302220072(A users){
/* I.S. terdefinisi tipe bentukan A yang berisi sejumlah A.nUser pemain pada array A.info
   F.S. menampilkan semua data pemain pada array A.info */
	for i := 0; i < A.nUser; i++ {
		fmt.Println(A.info[i])
   }
}

func setup_permainan_1302220072(left, right *island){
/* I.S. -
   F.S. left.nMember bernilai 0 dan right.nMember bernilai 5, sedangkan right.member berisi 1, 3, 6, 8, dan 12 */
    right.member = [NMAX]int{1, 3, 6, 8, 12}
    right.nMember = 5
	left.nMember = 0
}

func sequential_search_1302220072(A island, x int) int {
/* mengembalikan indeks dari x di dalam array A.member, atau -1 apabila tidak ditemukan */
	for i := 0; i < A.nMember; i++ {
		if A.member[i] == x {
			return i
		}
	}
	return -1
}

func add_member_1302220072(A *island, x int){
/* I.S. terdefinisi tipe bentukan A yang berisi array A.info sebanyak A.nMember elemen. dan sebuah bilangan bulat x
   F.S. menambahkan x kedalam array A.info dan A.nMember bertambah 1, apabila array penuh tampilkan "Pulau telah penuh"*/
	A.member[A.nMember] = x
	A.nMember++
}

func del_member_1302220072(A *island, x int){
/* I.S. terdefinisi tipe bentukan A yang berisi array A.info sebanyak A.nMember elemen. dan sebuah bilangan bulat x
   F.S. menghapus elemen dengan nilai x  dari array A.info, dan A.nMember berkurang 1, apabila x tidak ditemukan maka tampilkan "Orang yang dicari tidak ditemukan"*/
    if A.nMember != 0 {
        // lakukan pencarian x di dalam A dengan memanggil fungsi sequential_search
        var idx = sequential_search(A, x)
        // apabila data ditemukan maka lakukan proses penghapusan
        if idx != -1 {
            for i := idx; i < A.nMember; i++ {
				A.member[i] = A.member[i+1]
			}
			A.nMember--
        }else{
            fmt.Println("Tidak ditemukan")
        }
    }
}

func print_step_1302220072(left, right island, time int){
/* I.S. terdefinisi tipe bentukan left dan right yang berisi left.nMember dan right.nMember orang, serta sebuah bilangan bulat time
   F.S. menampilkan array left.member dan right.member serta sisa waktu secara horizontal */
    fmt.Print(" Kiri: ")
    var i int
    // tampilkan isi array left.member secara horizontal
	for i = 0; i < left.nMember; i++ {
		fmt.Print(left.member[i], "")
	}
    fmt.Print("\t\t Kanan: ")
    // tampilkan isi array right.member secara horizontal
	for i = 0; i < right.nMember; i++
		fmt.Print(right.member[i], "")
	}
    // tampilkan selisih waktu dengan LAMPLIFE
    LAMPLIFE - time
    fmt.Println(" --------------------------- \n")
}

func max_1302220072(a,b int) int{
/* mengembalikan nilai terbesar antara bilangan bulat a dan b*/
    ...
}

func move_1302220072(left, right *island, play bridge, time *int){
/* I.S. terdefinisi tipe bentukan left dan right yang berisi left.nMember dan right.nMember orang, play berisi sepasang orang yang menyeberang jembatan, serta sebuah bilangan bulat time
    F.S. left dan right terupdate sesuai dengan nilai pada play.m1 dan play.m2. Time terakumulasi dengan nilai terbesar antara play.m1 dan play.m2*/
    ...
}

func back_1302220072(left, right *island, play bridge, time *int){
/* I.S. terdefinisi tipe bentukan left dan right yang berisi left.nMember dan right.nMember orang, play.m1 berisi orang yang kembali, serta sebuah bilangan bulat time
    F.S. left dan right terupdate sesuai dengan nilai pada play.m1. Time terakumulasi dengan nilai play.m1*/
    ...
}

func mulai_permainan_1302220072(A *users){
/* I.S. terdefinisi tipe bentukan A yang berisi sejumlah A.nUser pemain pada array A.info
   proses:
   1. setup permainan
   2. menerima masukan berupa username pemain baru.
   3. berisi algoritma permaian bridge crossing hingga selesai
   F.S. array A.info bertambah 1 data pemain, nilai A.nUser bertambah 1*/
    // a. deklrasi variabel string nama dan integer time (inisilisasi dengan 0) untuk menyimpan data pemain.
    ...
    ...
    // b. deklrasikan variabel untuk pulau kiri dan kanan (bertipe island) dan variabel play beripe bridge.
    ...
    ...
    // c. lakukan setup permainan dengan memanggil procedure setup_permainan().
    ...
    // d. panggil procedure header dan minta masukan nama pemain.
    ...
    fmt.Print(...); fmt.Scan(...)
    fmt.Println(" Mulai permainan... ")
    // e. buatlah perulangan while dengan kondisi selama di pulau kanan masih ada orang.
    for ... {
        // f. tampilkan step saat ini dengan memanggil print_step.
        ...
        // g. minta masukan untuk pasangan orang yang akan menyeberang.
        fmt.Println(" Menyeberang (lihat di seberang kanan)...")
        ...
        ...
        // i. move() untuk pasangan orang yang akan menyeberang.
        ...
        // j. tampilkan step saat ini dengan memanggil print_step.
        ...
        // k. jika masih terdapat orang di pulau kanan maka
        if ... {
            fmt.Println(" Kembali...(lihat di seberang kiri)")
            // l. minta masukan untuk orang yang akan kembali mengantar lampu
            ...
            // m. back() untuk orang yang kembali mengantar lampu.
            ...
        }
    }
    // n. tambahkan data pemain ke dalam A
    ...
    ...
    A.nUser++
    // o. Tampilkan waktu yang dihabiskan pemain "Selesai, dengan waktu: x"
    ...
}

func main(){
    // deklarasi variabel
    ...
    // panggil procedure menu
    ...
}
