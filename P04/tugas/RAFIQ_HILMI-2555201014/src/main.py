
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def uji_validasi_tarif(traktor: AlatTani) -> None:
    """Menguji penolakan tarif yang tidak valid."""
    print("\n--- Percobaan menembus penjagaan ---")

    for tarif in (0, -5000):
        try:
            traktor.tarif_harian = tarif
        except ValueError as e:
            print(f"Ditolak (tarif {tarif}):", e)

    print("Tarif tetap utuh:", traktor.keterangan())


def tampilkan_pemeriksaan_tarif() -> None:
    """Menampilkan hasil pemeriksaan beberapa tarif."""
    print("\n--- Pemeriksaan tarif ---")

    for calon in (5000, 150000, 6000000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon):>14} → {status}")


def main() -> None:
    alamat_budi = Alamat("Pulau Jambu", "Kuok", "Kuok")

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)

    print(budi.identitas())
    print(alamat_budi.lengkap())
    print(traktor.keterangan())

    uji_validasi_tarif(traktor)
    tampilkan_pemeriksaan_tarif()

    print("\n--- Membuat alat dari baris CSV ---")
    pompa = AlatTani.dari_baris_csv("PA-01;Pompa Air;75000")
    print(pompa.keterangan())

    print("\n--- Jumlah alat terdaftar ---")
    print(AlatTani.jumlah_terdaftar())

    print("\n--- Denda keterlambatan ---")
    print(AlatTani.format_rupiah(traktor.denda_keterlambatan(2)))


if __name__ == "__main__":
    main()
