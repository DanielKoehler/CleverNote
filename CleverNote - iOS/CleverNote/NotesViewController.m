//
//  ViewController.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import "Note.h"
#import "NotesViewController.h"
#import "NotesTableViewCell.h"

@interface NotesViewController ()

@end

@implementation NotesViewController


- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    [self.navigationController.navigationBar setBarTintColor:[UIColor whiteColor]];
    
    [self.notesView setDelegate:self];
    [self.notesView setDataSource:self];
    
    [self.notesView registerClass:[NotesTableViewCell class] forCellReuseIdentifier:@"noteCellClassful"];
    
    self.notes = @[[[Note alloc] testNote], [[Note alloc] testNote]];
    
//  Registration View
    
//    self.signInViewController = [[SignInViewController alloc] init];
//    UINavigationController *signInNavigationController = [[UINavigationController alloc] initWithRootViewController:self.signInViewController];
//    
//    
//    [self presentViewController:signInNavigationController animated:NO completion:nil];
    
    
}


- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;    //count of section
}


- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    
    return [self.notes count];

}



-(UITableViewCell *) tableView:(UITableView *)tableView
cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = @"noteCell";
    
    NotesTableViewCell *cell = (NotesTableViewCell *)[self.notesView dequeueReusableCellWithIdentifier:CellIdentifier];
    
    cell.note = self.notes[indexPath.row];
    
    [cell awakeFromNib];
    
//    cell.backgroundColor = [UIColor blueColor];
    
    return cell;
    
}



- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
} 

@end
