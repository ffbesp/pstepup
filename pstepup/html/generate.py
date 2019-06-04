
import appdata
import home
import about
import bannerlist
import banner


def main():
    home.main()
    about.main()
    bannerlist.main()

    for banner_id in appdata.banner_info:
        banner.create_banner_page(banner_id)


if __name__ == '__main__':
    main()