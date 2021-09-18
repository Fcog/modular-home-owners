from wagtail.core import blocks
from wagtail.core import fields
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from .HeadingH1 import HeadingH1
from .Paragraph import Paragraph
from .Buttons import Buttons
from .ReadMoreText import ReadMoreText
from .BlueBoxCTA import BlueBoxCTA
from .ArticlesLinksBox import ArticlesLinksBox
from .IconsGrid import IconsGrid


class AvailableColumnBlocks(blocks.StreamBlock):
    headingH1 = HeadingH1()
    paragraph = Paragraph()
    readMoreText = ReadMoreText()
    buttons = Buttons()
    blueBoxCTA = BlueBoxCTA()
    iconsGrid = IconsGrid()
    ArticlesLinksBox = ArticlesLinksBox()
    quote = blocks.BlockQuoteBlock()
    image = ImageChooserBlock()
    embed = EmbedBlock()
