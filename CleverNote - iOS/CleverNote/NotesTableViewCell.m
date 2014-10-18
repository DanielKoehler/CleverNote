//
//  NotesTableViewCell.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import "TagCollectionViewCell.h"
#import "NotesTableViewCell.h"

@implementation NotesTableViewCell

- (void) awakeFromNib {
    // Initialization code
    
    [super awakeFromNib];

    
    self.titleLabel.text  = self.note.title;
    self.excerpLabel.text = self.note.content;
    
    NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
    [formatter setDateFormat:@"dd/mm/yyyy"];
    
//    [formatter setTimeZone:[NSTimeZone timeZoneWithName:@"gmt"]];
    
    NSString *stringFromDate = [formatter stringFromDate:self.note.updated];
    
    self.dateLabel.text = stringFromDate;
    
    [self.tagCollectionView setDelegate:self];
    [self.tagCollectionView setDataSource:self];
    [self.tagCollectionView setUserInteractionEnabled:NO];
    
//    [self.tagCollectionView registerClass:[TagCollectionViewCell class] forCellWithReuseIdentifier:@"Cell"];

}

-(NSInteger)numberOfSectionsInCollectionView:(UICollectionView *)collectionView {
    return 1;
}

-(NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section {
    return [self.note.tags count];
}


-(UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath {
    
    TagCollectionViewCell *cell = [self.tagCollectionView dequeueReusableCellWithReuseIdentifier:@"tagCell" forIndexPath:indexPath];
    
    cell.backgroundColor = [UIColor whiteColor];
    cell.title = self.note.tags[indexPath.row];
    
    return cell;
    
}

-(CGSize)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout*)collectionViewLayout sizeForItemAtIndexPath:(NSIndexPath *)indexPath {
    
    return CGSizeMake([self.note.tags[indexPath.row] length] * 6.6, 30);

}



- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
