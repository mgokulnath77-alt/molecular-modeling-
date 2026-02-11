import flet as ft
import time

def main(page: ft.Page):
    page.title = "ArthroDock: COX-2 & Ibuprofen Lab"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 1200
    page.window.height = 800
    page.padding = 0
    page.fonts = {
        "Poppins": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Poppins")

    # --- Background Styling ---
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.ControlDecoration(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.BLACK, ft.colors.INDIGO_900, ft.colors.BLUE_900],
        )
    )

    # --- State Management ---
    current_step = ft.Ref[ft.Text]()

    # --- Reusable Glassmorphism Card ---
    def GlassCard(content, width=None, height=None, padding=20):
        return ft.Container(
            content=content,
            width=width,
            height=height,
            padding=padding,
            border_radius=20,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.WHITE)),
            blur=ft.Blur(15, 15),
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.colors.with_opacity(0.1, ft.colors.BLACK))
        )

    # --- Sections ---
    
    # 1. Sidebar
    sidebar = ft.Container(
        content=ft.Column([
            ft.Text("ARTHRO", size=24, weight="bold", color=ft.colors.CYAN_400),
            ft.Divider(color=ft.colors.WHITE24),
            ft.ListTile(leading=ft.Icon(ft.icons.DASHBOARD), title=ft.Text("Dashboard")),
            ft.ListTile(leading=ft.Icon(ft.icons.UPLOAD_FILE), title=ft.Text("Upload Data")),
            ft.ListTile(leading=ft.Icon(ft.icons.SCIENCE), title=ft.Text("Docking Lab")),
            ft.ListTile(leading=ft.Icon(ft.icons.ANALYTICS), title=ft.Text("Interactions")),
        ], spacing=20),
        width=250,
        padding=20,
        bgcolor=ft.colors.with_opacity(0.05, ft.colors.BLACK),
    )

    # 2. Progress Header
    progress_row = ft.Row([
        ft.Container(content=ft.Text("Start", color="white"), bgcolor="green", padding=10, border_radius=10),
        ft.Icon(ft.icons.ARROW_FORWARD, size=16),
        ft.Container(content=ft.Text("Upload", color="white"), bgcolor="blue", padding=10, border_radius=10),
        ft.Icon(ft.icons.ARROW_FORWARD, size=16),
        ft.Container(content=ft.Text("Docking", color="white"), bgcolor="grey", padding=10, border_radius=10),
        ft.Icon(ft.icons.ARROW_FORWARD, size=16),
        ft.Container(content=ft.Text("Analysis", color="white"), bgcolor="grey", padding=10, border_radius=10),
    ], alignment=ft.MainAxisAlignment.CENTER)

    # 3. Stats Section (The Results)
    stats_cards = ft.Row([
        GlassCard(ft.Column([
            ft.Text("Binding Affinity", size=14, color=ft.colors.WHITE70),
            ft.Text("-8.4 kcal/mol", size=28, weight="bold", color=ft.colors.CYAN_accent)
        ]), expand=1),
        GlassCard(ft.Column([
            ft.Text("H-Bonds", size=14, color=ft.colors.WHITE70),
            ft.Text("3 Active", size=28, weight="bold", color=ft.colors.GREEN_accent)
        ]), expand=1),
        GlassCard(ft.Column([
            ft.Text("Stability", size=14, color=ft.colors.WHITE70),
            ft.Text("High", size=28, weight="bold", color=ft.colors.PURPLE_accent)
        ]), expand=1),
    ], spacing=20)

    # 4. Interaction Table
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Residue")),
            ft.DataColumn(ft.Text("Type")),
            ft.DataColumn(ft.Text("Distance (Å)")),
        ],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text("ARG-120")), ft.DataCell(ft.Text("H-Bond")), ft.DataCell(ft.Text("2.81"))]),
            ft.DataCell(ft.Text("TYR-355")), ft.DataCell(ft.Text("vdw")), ft.DataCell(ft.Text("3.42")),
        ]
    )

    # --- Main Layout Assembly ---
    main_content = ft.Column([
        ft.Text("Computational Evaluation: Ibuprofen vs COX-2", size=32, weight="bold"),
        ft.Text("Targeting Arthritis Inflammation via Molecular Docking", color=ft.colors.WHITE70),
        ft.VerticalDivider(height=20, color=ft.colors.TRANSPARENT),
        progress_row,
        ft.VerticalDivider(height=20, color=ft.colors.TRANSPARENT),
        stats_cards,
        ft.VerticalDivider(height=20, color=ft.colors.TRANSPARENT),
        GlassCard(ft.Column([
            ft.Text("Recent Docking Poses & Interactions", size=18, weight="bold"),
            table
        ]), width=900)
    ], scroll=ft.ScrollMode.AUTO, expand=True, spacing=10)

    # Final Page Layout
    page.add(
        ft.Row([
            sidebar,
            ft.Container(content=main_content, padding=40, expand=True)
        ], expand=True)
    )

ft.app(target=main)
