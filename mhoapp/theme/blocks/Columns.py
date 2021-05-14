from wagtail.core import blocks
from wagtail.core import fields
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtailcolumnblocks.blocks import ColumnsBlock

from .HeadingH1 import HeadingH1
from .Paragraph import Paragraph
from .ReadMoreText import ReadMoreText
from .BlueBoxCTA import BlueBoxCTA


class AvailableColumnBlocks(blocks.StreamBlock):
    headingH1 = HeadingH1()
    paragraph = Paragraph()
    readMoreText = ReadMoreText()
    blueBoxCTA = BlueBoxCTA()
    quote = blocks.BlockQuoteBlock()
    image = ImageChooserBlock()
    embed = EmbedBlock()


class TwoColumnsBlock(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    two_columns = ColumnsBlock(
        # Blocks you want to allow within each column
        AvailableColumnBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        template='patterns/organisms/sections/two-cols.html',
    )


class TwoColumnsBlockEqualWidth(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    two_columns = ColumnsBlock(
        # Blocks you want to allow within each column
        AvailableColumnBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        template='patterns/organisms/sections/two-cols-equal-width.html',
    )


class TwoColumnsLeftShorterBlock(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    two_columns = ColumnsBlock(
        # Blocks you want to allow within each column
        AvailableColumnBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        template='patterns/organisms/sections/two-cols-left-shorter.html',
    )    