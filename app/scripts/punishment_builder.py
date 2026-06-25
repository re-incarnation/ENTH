class PunishmentBuilder:


    @staticmethod
    def ban(
        player,
        time,
        reason
    ):

        return (
            f"/tempban "
            f"{player} "
            f"{time} "
            f"{reason}"
        )



    @staticmethod
    def mute(
        player,
        time,
        reason
    ):

        return (
            f"/tempmute "
            f"{player} "
            f"{time} "
            f"{reason}"
        )



    @staticmethod
    def warn(
        player,
        reason
    ):

        return (
            f"/warn "
            f"{player} "
            f"{reason}"
        )