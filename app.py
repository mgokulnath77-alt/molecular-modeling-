import flet as ft
import os

def main(page: ft.Page):
    page.title = "COX-2 Analyzer | Team 3 Lab"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    
    # Apple + Bioinformatics Styling
    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.ControlDecoration(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#0f172a", "#1e1b4b", "#581c87"],
        )
    )

    # --- Reusable Components ---
    def glass_card(content, expand=False):
        return ft.Container(
            content=content,
            padding=20,
            border_radius=20,
            expand=expand,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            border=ft.border.all(1, ft.colors.with_opacity(0.1, ft.colors.WHITE)),
            blur=ft.Blur(20, 20),
        )

    # --- Sidebar Navigation ---
    sidebar = ft.Container(
        width=250,
        padding=30,
        bgcolor=ft.colors.with_opacity(0.05, ft.colors.BLACK),
        content=ft.Column([
            ft.Text("ARTHRO LAB", size=24, weight="bold", color=ft.colors.CYAN_400),
            ft.Divider(color=ft.colors.WHITE24),
            ft.TextButton("DASHBOARD", icon=ft.icons.DASHBOARD_ROUNDED, icon_color="cyan"),
            ft.TextButton("MOLECULAR VIEW", icon=ft.icons.VIEW_IN_AR_ROUNDED, icon_color="purple"),
            ft.TextButton("REPORT GEN", icon=ft.icons.DESCRIPTION_ROUNDED, icon_color="white"),
        ], spacing=15)
    )

    # --- Stats Cards ---
    stats = ft.Row([
        glass_card(ft.Column([
            ft.Text("Binding Affinity", size=14, color=ft.colors.WHITE70),
            ft.Text("-8.4 kcal/mol", size=30, weight="bold", color=ft.colors.CYAN_ACCENT),
        ]), expand=True),
        glass_card(ft.Column([
            ft.Text("H-Bonds", size=14, color=ft.colors.WHITE70),
            ft.Text("3 Active", size=30, weight="bold", color=ft.colors.GREEN_ACCENT),
        ]), expand=True),
        glass_card(ft.Column([
            ft.Text("Stability", size=14, color=ft.colors.WHITE70),
            ft.Text("High", size=30, weight="bold", color=ft.colors.PURPLE_ACCENT),
        ]), expand=True),
    ], spacing=20)

    # --- Main Dashboard Body ---
    body = ft.Column([
        ft.Text("Computational Evaluation: Ibuprofen vs COX-2", size=32, weight="bold"),
        ft.Text("Module: Protein–Ligand Interaction | Project Title: Arthritis Treatment Analysis", color=ft.colors.WHITE70),
        ft.Container(height=20),
        stats,
        ft.Container(height=20),
        glass_card(ft.Column([
            ft.Text("Interaction Analysis Table", size=20, weight="bold"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Residue")),
                    ft.DataColumn(ft.Text("Interaction Type")),
                    ft.DataColumn(ft.Text("Distance (Å)")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("ARG-120")), ft.DataCell(ft.Text("Hydrogen Bond")), ft.DataCell(ft.Text("2.81"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("TYR-355")), ft.DataCell(ft.Text("van der Waals")), ft.DataCell(ft.Text("3.42"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("VAL-523")), ft.DataCell(ft.Text("Hydrophobic")), ft.DataCell(ft.Text("4.15"))]),
                ]
            )
        ])),
    ], expand=True, scroll=ft.ScrollMode.AUTO)

    # --- Final Layout ---
    page.add(
        ft.Row([
            sidebar,
            ft.Container(content=body, padding=40, expand=True)
        ], expand=True)
    )

# --- THE FIX FOR YOUR ERROR ---
if __name__ == "__main__":
    # We use view=ft.AppView.WEB_BROWSER to avoid signal handler issues on hosted servers
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
