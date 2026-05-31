import csv
from datetime import datetime
from collections import defaultdict

from pep_parse.constants import DOWNLOAD_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.counts: defaultdict[str, int] = defaultdict(int)

    def process_item(self, item, spider):
        self.counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        DOWNLOAD_DIR.mkdir(exist_ok=True)
        filename_ = f'status_summary_{current_time}.csv'
        results_path = DOWNLOAD_DIR / filename_
        with open(results_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(zip(self.counts, self.counts.values()))
            writer.writerow(('Total', sum(self.counts.values())))
